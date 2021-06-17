import requests


def get_status(tracking_number):
    my_headers = {
        'Authorization': 'aGNEdjJhYktkdG9PcHQxS2ppcDFvNVZLMmFOWUxneXdVaEdyUlBDdGJ1dDJ0MTZYVm1LUW1xQXo4RnBH606c475a94588'
    }

    data = {'tracking_number': tracking_number, 'type': 0}
    status = requests.get(
        'https://sonic.pk/api/shipment/status?tracking_number={}&type={}'.format(tracking_number, 0),
        headers=my_headers, data=data)

    return status.json().get("current_status")
