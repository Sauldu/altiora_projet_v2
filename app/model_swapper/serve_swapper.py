# app/model_swapper/serve_swapper.py
import ray
from ray import serve
import os, torch, gc

@serve.deployment(
    ray_actor_options={"num_gpus": 1, "memory": 20 * 1024**3},  # 20 GB
    max_ongoing_requests=1,
    autoscaling_config={"min_replicas": 1, "max_replicas": 1}
)
class ModelSwapper:
    def __init__(self):
        self._models = {}

    @serve.multiplexed(max_num_models_per_replica=1)   # LRU = 1 modèle en RAM
    async def load_model(self, model_id: str):
        if model_id == "qwen3-32b":
            return torch.load("models/qwen3-32b.pth", map_location="cuda")
        if model_id == "starcoder2-15b":
            return torch.load("models/starcoder2-15b.pth", map_location="cuda")
        raise ValueError("unknown model")

    async def __call__(self, request):
        model_id = serve.get_multiplexed_model_id()
        model = await self.load_model(model_id)
        return {"status": "loaded", "model": model_id}

app = ModelSwapper.bind()