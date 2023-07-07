# From host
## on `error action request
```json
{
    "action" : "error",
    "content" : "error content"
}
```

## on `add` action request
```json
{
    "action" : "add",
    "controls" : [
        {
            "name" : "<flet_class_name>",
            "number" : "<flet_lite_control_number>",
            "flet_class_dict" : {},
            "parent" : "Page/<flet_lite_control_number>",
            "overlay" : false
        }
    ]
}
```

## on `page_update` request
```json
{
    "action" : "page_update",
    "props" : {},
    "page_custom_controls" : {
        "appbar" : {"bgcolor" : "white"}
    }
}
```

## on control `update` request
```json
{
    "action" : "update",
    "controls" : [
        {
            "number" : "<flet_lite_control_number>",
            "flet_class_dict" : {}
        }
    ]
}
```

## on control `clean` request
```json
{
    "action" : "clean",
    "control_number" : "page/flet_lite_control_number"
}
```

## on control `remove` request
```json
{
    "action" : "remove",
    "controls_numbers" : [1, 2, 4, 7]
}
```

# From browser

## push event updates
```json
{
    "event_name" : "resize",
    "flet_class_number" : "",
    "data" : ""
}
```