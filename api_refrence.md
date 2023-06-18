
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
    "control_data" : {
        "name" : "",
        "number" : <Number of the control>,
        "flet_class_dict" : {}
    }
}
```

## on `page_update` request
```json
{
    "action" : "page_update",
    "props" : {},
    "appbar_class_props" : {
        "bgcolor" : "white"
    }
}
```

## on control `update` request
```json
{
    "action" : "update",
    "control_data" : {
        "control_number" : <number>,
        "flet_class_dict" : {}
    }
}
```