from openks.mm.pipeline import Pipeline
from openks.mm.data_loader import GlobDataLoader
from openks.models.pytorch.mmd_modules.clip import CLIP


def main():
    pipeline = Pipeline(
        GlobDataLoader(root_dir="../datasets/images"),
        CLIP("ViT-B/32", jit=False),
        # Detection or Scene Graph models
    )
    graph = pipeline.run()
    graph.save("../datasets/test-kg")


if __name__ == "__main__":
    main()
