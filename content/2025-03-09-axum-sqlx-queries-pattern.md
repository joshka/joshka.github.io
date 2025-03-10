+++
title = "An ergonomic pattern for SQLx queries in Axum"
date = "2025-03-09T18:08:00-07:00"
[taxonomies]
tags = ["Software", "Rust"]
+++

Axum is the most popular web framework in Rust at the time of writing. In this post, I'll show an
easy and ergonomic pattern for connecting to a database using SQLx and Axum.

This is a small response to a question on [a reddit thread about how to structure SQLx queries in
Axum](https://www.reddit.com/r/rust/comments/1j76nhm/comment/mgy2ptm/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button).
The pattern I'll show here is not the only way to do it, but it's one that I've found to be simple
and effective.

TL;DR: Store the database pool in your application state, create a struct to hold your queries, and
use the `FromRef` trait to simplify the interaction between your handlers and the database.

<!-- more -->

## The problem

When writing web applications, you often need to interact with a database. In Rust, one of the the
most popular database libraries is SQLx. Setting up SQLx with Axum is straightforward, but it can be
a bit repetitive. You need to create a database pool, pass it to your handlers, and then use it in
your queries.

For the purpose of this post, let's assume you have a simple web application that interacts directly
with a Sqlite database rather than through some ORM or other service abstraction. This is common for
smaller projects or when you want to keep things simple.

Here's an example of how you might set up SQLx with Axum:

```rust
type Db = sqlx::SqlitePool;
type Result<T, E> = std::result::Result<T, E = crate::Error>; // or use anyhow / color-eyre

#[derive(Clone)]
struct AppState {
    db: Db,
}

#[tokio::main]
async fn main() -> Result<()> {
    // ... other config code ...
    
    let db = Db::connect(config.connection_string).await?;
    let state = AppState { db };

    let app = Router::new()
        .nest("/users", users::router())
        .nest("/posts", posts::router())
        // ... other routes ...
        .with_state(state);
    
    // ... other server setup code ...
}
```

```rust
mod users {
    use axum::{extract::{FromRequest, Path}, response::Json, Router};
    use sqlx::query;

    use super::{AppState, Db};

    #[derive(sqlx::FromRow)]
    struct User {
        id: i32,
        name: String,
    }

    pub fn router() -> Router {
        Router::new()
            .route("/", get(index))
            .route("/:id", get(show))
    }

    async fn index(state: AppState) -> Result<Json<Vec<User>>> {
        let users = query!("SELECT * FROM users")
            .fetch_all(&state.db)
            .await?;
        Ok(Json(users))
    }

    async fn show(state: AppState, id: Path<i64>) -> Result<Json<User>> {
        let user = query!("SELECT * FROM users WHERE id = ?", id)
            .fetch_one(&state.db)
            .await?;
        Ok(Json(user))
    }

    // ... other handlers ...
}
```

The two main issues with this approach are:

1. The queries are scattered throughout the handlers, making it hard to see what queries are
   available and where they are used.
2. The code for extracting the database pool from the state is repeated in every handler.

## The solution

To make this process simpler, we can create a type in each vertical slice which holds the logic for
all the queries in the module and implement the `FromRef` trait for it. This trait allows us to pass
a State extractor to our handlers which is scoped to only the queries struct related to the module.

Here's how you might refactor the above example:

```rust
mod users {
    use axum::{extract::{FromRequest, Path}, response::Json, Router};
    use sqlx::query;

    use super::{AppState, Db};

    #[derive(sqlx::FromRow)]
    struct User {
        id: i32,
        name: String,
    }

    pub struct Users {
        db: sqlx::SqlitePool,
    }

    impl FromRef<AppState> for Users {
        fn from_ref(state: &AppState) -> Self {
            let db = state.db.clone();
            Self { db }
        }
    }

    impl Users {
        pub fn new(db: Db) -> Self {
            Self { db }
        }

        pub async fn all(&self) -> sqlx::Result<Vec<User>> {
            query!("SELECT * FROM users")
                .fetch_all(&self.db)
                .await
        }

        pub async fn find_by_id(&self, id: i64) -> Result<User> {
            query!("SELECT * FROM users WHERE id = ?", id)
                .fetch_one(&self.db)
                .await
        }

        // ... other queries ...
    }

    async fn index(queries: State<Users>) -> Result<Json<Vec<User>>> {
        let users = queries.index().await?;
        Ok(Json(users))
    }

    async fn show(queries: State<Users>, id: Path<i64>) -> Result<Json<User>> {
        let user = queries.find_by_id(*id).await?;
        Ok(Json(user))
    }

    // ... other handlers ...
}
```

Using this pattern lets the infrastructure code be separated from the handlers. The `Users` struct
is automatically created from the state and passed to the handlers. This makes the handlers cleaner
and easier to read as they avoid the need to extract the database pool from the state.

This approach provides a nice separation of concerns. The `Users` struct is responsible for
interacting with the database, while the handlers are responsible for handling the HTTP requests.

It also provides a seam for unit testing. You can easily mock the `Users` struct in your tests to
avoid hitting the database, as well as providing an ability to test the queries in isolation from
the handlers.
