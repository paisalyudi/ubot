
```
apt update && apt upgrade -y
```
```
git clone https://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@github.com/paisalyudi/ubot
```
```
cd ubot && screen -S ubot
```
```
bash installnode.sh && apt install python3.10-venv
```
```
python3 -m venv ubot && source ubot/bin/activate

```
```
pip3 install -r requirements.txt
```
```
cp sample.env .env && nano .env
```
```
python3 -m PyroUbot
```
