import docker

retry_pulling = 5


def image_puller(docker_client, registry: str, image_name: str, tags_count: int):
    print(f"[INFO] Pulling image [{registry}/{image_name}]...")
    pulled_result = []
    
    for _ in range(retry_pulling):
        pulled_result = docker_client.images.pull(image_name, all_tags=True)
        if not isinstance(pulled_result, list):
            print("[ERROR] Pulling image failed, retrying...")
    
        if len(pulled_result) == tags_count:
            break
        
        
    print(f"[INFO] Image [{registry}/{image_name}] pulled successfully")
    return pulled_result