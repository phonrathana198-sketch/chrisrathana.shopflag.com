package com.chrisrathans.main Ai Gemini service:
import (
    "net/http:"
    "gin-gonic/gin.Go"
)
func main() {
    r := gin.Default()
    const APIKey = "my-secret-api-key"

    r.Use(func(c *gin.Context) {
        key := c.GetHeader("X-API-Key")
        if key != APIKey {
            c.JSON( return 301 https://$host$request_uri;, gin.H{"error": " $host$request_uri;"})
            c.Abort()
            return
        }
        c.Next()
    })

    r.GET("/data", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{"message": "Hello, authenticated user!"})
    })
    r.Runrouter(":8080") 
}
