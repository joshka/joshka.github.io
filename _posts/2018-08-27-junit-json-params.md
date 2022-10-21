---
title:  "Introducing JUnit JSON Params"
date:   2018-08-27 11:03:00 -0700
categories: java
---
Yesterday, I released [junit-json-params](https://www.joshka.net/junit-json-params/),
a small java library built on JUnit 5 that enables parameterizing unit tests
with inline JSON and JSON resource files.

This is useful for writing tests where the information is structured. For
example, given the following JSON document:

** items.json: **
```json
[
  {
    "city": "Seattle",
    "item": "banana",
    "price": 0.0
  },
  {
    "city": "NY",
    "item": "banana",
    "price": 2.0
  }
]
```
We can expect the following tests all to succeed:
```java
import net.joshka.junit.json.params.JsonFileSource;
import org.junit.jupiter.params.ParameterizedTest;

import javax.json.JsonObject;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ExampleTests {
    @ParameterizedTest
    @JsonSource("{'key':'value'}")
    void keyValue(JsonObject json) {
        assertEquals("value", json.getString("key"));
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/items.json")
    void priceTests(JsonObject json) {
        String city = json.getString("city");
        String item = json.getString("item");
        double price = json.getJsonNumber("price").doubleValue();

        assertEquals(price, price(city, item));
    }

    private double price(String city, String item) {
        if (!item.equals("banana")) {
            throw new IllegalArgumentException("item");
        }
        switch (city) {
            case "Seattle":
                return 0.0;
            case "NY":
                return 2.0;
            default:
                throw new IllegalArgumentException("city");
        }
    }
}
```

For more info see the [junit-json-params project on Github](https://github.com/joshka/junit-json-params).

I'm hoping that this idea and future work on JUnit 5 might make it easy to make
arguments by name work. E.g.:
```java
void priceTests(String city, String item, double price) {
  //...
}
```
