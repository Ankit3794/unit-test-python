import requests
import responses


@responses.activate
def test_simulate_user2():
    responses.add(
        responses.GET,
        "https://reqres.in/api/users/2",
        json={"data": {"id": 2, "email": "ankit.patel@gmail.com", "first_name": "Ankit", "last_name": "Patel",
                       "avatar": "https://reqres.in/img/faces/2-image.jpg"},
              "support": {"url": "https://reqres.in/#support-heading",
                          "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}},
        status=200
    )

    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["data"]["first_name"] == "Ankit"
    assert response_body["data"]["last_name"] == "Patel"
    assert response_body["data"]["email"] == "ankit.patel@gmail.com"


@responses.activate
def test_simulate_user_create():
    expected_output = {
        "name": "Ankit",
        "job": "Patel",
        "id": "999",
        "createdAt": "2021-10-13T13:17:29.268Z"
    };
    responses.add(responses.POST, 'https://reqres.in/api/users',
                  json=expected_output, status=201)

    response = requests.post('https://reqres.in/api/users', params={
        "name": "morpheus",
        "job": "leader"
    })

    response_body = response.json()
    assert response_body == expected_output
