from typing import TypedDict
import yaml
import os

class TSettingsGame(TypedDict):
  frameRate: int
  mainScene: str
class TSettingsWindow(TypedDict):
  title: str
  dimension: "tuple[int, int]"
  fullScreen: bool
class TSettings(TypedDict):
  paths: "dict[str, str]"
  window: TSettingsWindow
  game: TSettingsGame
class ResolverConfig:
  __settings: TSettings = None
  def __init__(self):
    pass

  @staticmethod
  def resolve() -> TSettings:
    if(ResolverConfig.__settings is None):
      ResolverConfig.__settings = ResolverFile.readYaml(f"{ResolverPath.getLocalPath()}/settings.yaml")
    
    return ResolverConfig.__settings


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
  def getAllWithDir(path: str) -> "list[str]":
    return os.listdir(ResolverPath.resolve(path))
  
  @staticmethod
  def getAllFilesWithExtension(path: str, extension: str) -> "list[str]":
    files = []
    for file in ResolverFile.getAllWithDir(path):
      if file.endswith(extension):
        files.append(file)
    return files
  
  @staticmethod
  def read(path: str) -> str:
    try:
      with open(ResolverPath.resolve(path), "r") as file:
        read = file.read()
        file.close()
        return read
    except:
      raise Exception("File not found or not permission")
    
  @staticmethod
  def write(path: str, content: str) -> bool:
    try:
      with open(ResolverPath.resolve(path), "w") as file:
        file.write(content)
        file.close()
      return True
    except:
      return False

  @staticmethod
  def readYaml(path: str) -> dict:
    try:
      with open(ResolverPath.resolve(path), "r") as file:
        read = yaml.load(file, Loader=yaml.FullLoader)
        file.close()
        return read
    except:
      raise Exception("File not found or not permission")
    
  @staticmethod
  def writeYaml(path: str, content: dict) -> bool:
    try:
      with open(ResolverPath.resolve(path), "w") as file:
        yaml.dump(content, file)
        file.close()
      return True
    except:
      return False