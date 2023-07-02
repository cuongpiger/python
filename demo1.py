






def construct_span(tracer):
    with tracer.start_span('AliyunTestSpan') as span:
        span.log_kv({'event': 'test message', 'life': 42})
        print("tracer.tages: ", tracer.tags)
        with tracer.start_span('AliyunTestChildSpan', child_of=span) as child_span:
            span.log_kv({'event': 'down below'})
        return span

def construct_span2(tracer):
    with tracer.start_span('CuongDM') as span:
        span.log_kv({'event': 'test message', 'life': 42})
        print("tracer.tages: ", tracer.tags)
        with tracer.start_span('CuongDM3', child_of=span) as child_span:
            span.log_kv({'event': 'down below'})
        return span

