import yaml
import os

class ResolverConfig:
  def __init__(self):
    pass

  @staticmethod
  def resolve() -> dict:
    with open(f"{ResolverPath.getLocalPath()}/settings.yaml", "r") as file:
      return yaml.load(file, Loader=yaml.FullLoader)

class ResolverPath:
  def __init__(self):
    pass

  @staticmethod
  def resolve(path: str):
    paths = ResolverConfig.resolve()["paths"]
    for key in paths:
      path = path.replace(f"@{key}", paths[key])
      
    return f"{ResolverPath.getLocalPath()}/{path}"
  
  @staticmethod
  def getLocalPath():
    return os.getcwd()
    
class ResolverFile:
  def __init__(self):
    pass

  @staticmethod
  def getAllFiles(path: str) -> "list[str]":
    return os.listdir(ResolverPath.resolve(path))