import pytest
import json
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api import app, ScheduleData, ScheduleOptimizer

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_health(client):
    r = client.get('/health')
    assert r.status_code == 200
    assert json.loads(r.data)['status'] == 'ok'

def test_index(client):
    r = client.get('/')
    assert r.status_code == 200

def test_calculate_success(client):
    r = client.post('/calculate',
                    data=json.dumps({'max_iterations': 5, 'population_size': 10}),
                    content_type='application/json')
    assert r.status_code == 200
    assert json.loads(r.data)['status'] == 'success'

def test_calculate_fields(client):
    r = client.post('/calculate',
                    data=json.dumps({'max_iterations': 5, 'population_size': 10}),
                    content_type='application/json')
    result = json.loads(r.data)['result']
    for f in ('conflicts', 'gaps', 'final_score', 'schedule_preview'):
        assert f in result

def test_conflicts_non_negative(client):
    r = client.post('/calculate',
                    data=json.dumps({'max_iterations': 3, 'population_size': 5}),
                    content_type='application/json')
    assert json.loads(r.data)['result']['conflicts'] >= 0

def test_schedule_data():
    d = ScheduleData(5, 10, 4, 3)
    assert len(d.lecturers) == 5
    assert len(d.subjects)  == 10

def test_optimizer():
    d   = ScheduleData(3, 5, 3, 2)
    opt = ScheduleOptimizer(d, population_size=5, max_iterations=3)
    s   = opt.optimize()
    assert len(s) == 5
    assert opt.check_conflicts(s) >= 0
