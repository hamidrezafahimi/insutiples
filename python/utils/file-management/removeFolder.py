from pathlib import Path

def removeDirectory(directory):
    directory = Path(directory)
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()

removeDirectory(Path('../../../nn_samples/data/logs/q_learning_frozenLake/'))