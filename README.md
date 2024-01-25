# video-recorder-rest-backend
A Flask Backend that used opencv-python-headless to capture video from default cam, store to file storage

### Pre-reqs
1. Python 3+
2. Equivalent, Compatible `pip`
3. Flask, opencv-python-headless

### Run Backend
`python index.py`

1. To start video capture, send a POST request to http://localhost:5000/start
2. To stop video capture and save the file, send a POST request to http://localhost:5000/stop

### Tested Enviroments
- [x] macos (14.2.1 (23C71))
- [ ] windows: TBD
- [ ] linux: TBD