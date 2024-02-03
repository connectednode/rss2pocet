package main

import (
	"fmt"
	"github.com/mmcdole/gofeed"
)

func main() {
    parser := gofeed.NewParser()
    feed, _ := parser.ParseURL("https://blog.ironsm4sh.nl/feed.xml")
    fmt.Println(feed.Link,feed.Items[0].Link,feed.Items[0].GUID)
}

