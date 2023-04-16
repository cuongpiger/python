###### References
- CSDN - [https://blog.csdn.net/weixin_36179862/article/details/123485035](https://blog.csdn.net/weixin_36179862/article/details/123485035)

###### Brief
- Using Open-Telemetry and Jaeger to tracing between microservices.

###### Guideline
* Run Jaeger inside Docker container.
  ```bash
  docker run -d --name jaeger \
    -e COLLECTOR_ZIPKIN_HTTP_PORT=:9411 \
    -e COLLECTOR_OTLP_ENABLED=true \
    -p 6831:6831/udp \
    -p 6832:6832/udp \
    -p 5778:5778 \
    -p 16686:16686 \
    -p 4317:4317 \
    -p 4318:4318 \
    -p 14250:14250 \
    -p 14268:14268 \
    -p 14269:14269 \
    -p 9411:9411 \
    jaegertracing/all-in-one:1.37
  ```