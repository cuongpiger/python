###### References
- CSDN - [https://blog.csdn.net/rgc_520_zyl/article/details/126710526](https://blog.csdn.net/rgc_520_zyl/article/details/126710526)

###### Brief
- Using Open-Telemetry and Jaeger, Flask.

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

* Create the Python virtual environment:
  ```bash
  conda create -n opentelemetry python=3.8 pip
  ```
  
* Run the Flask application:
  ```bash
  python main.py
  ```
* Send the `curl` request:
  ```bash
  curl 0.0.0.0:8000/roll
  ```
  ![](./img/01.png)

* Check the Jaeger UI to see the result:
  ![](./img/02.png)
  ![](./img/03.png)
