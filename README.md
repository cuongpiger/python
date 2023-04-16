###### Reference
- Medium - [https://medium.com/velotio-perspectives/a-comprehensive-tutorial-to-implementing-opentracing-with-jaeger-a01752e1a8ce](https://medium.com/velotio-perspectives/a-comprehensive-tutorial-to-implementing-opentracing-with-jaeger-a01752e1a8ce)

###### Brief
* Tracing in Python with Jaeger and Docker.

###### Guideline
- Run the Jaeger in Docker container.
  ```bash
  docker run --name jaeger -d -p6831:6831/udp -p16686:16686 jaegertracing/all-in-one:1.44
  ```
  
- Prepare the Python environment.
  ```bash
  conda create -n jaeger-tracing python=3.10 pip
  ```
  
- Run the Python script.
  ```bash
  python main.py batman
  ```
  
- See the result on Jaeger UI on [http://localhost:16686](http://localhost:16686).
  ![](./img/01.png)