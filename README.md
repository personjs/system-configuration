# System Configuration

## Setup

```shell
# Ubuntu
sudo apt-get install libxcb-xinerama0
```

## Development

```shell
# Having issues installing pyqt5?
poetry cache clear --all pypi
poetry env remove python
poetry shell
pip install pyqt5
pip freeze > requirements.txt
poetry add $(cat requirements.txt)
```
