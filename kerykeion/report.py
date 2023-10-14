import json
from kerykeion import AstrologicalSubject

class Report:
    """
    Create a report for a Kerykeion instance.
    """

    def __init__(self, instance: AstrologicalSubject):
        self.instance = instance

    def get_report_title(self) -> dict:
        return {"title": f"Report for {self.instance.name}"}

    def get_data_table(self) -> dict:
        return {
            "data": {
                "Date": f"{self.instance.day}/{self.instance.month}/{self.instance.year}",
                "Time": f"{self.instance.hour}:{self.instance.minute}",
                "Location": f"{self.instance.city}, {self.instance.nation}",
                "Longitude": self.instance.lng,
                "Latitude": self.instance.lat,
            }
        }

    def get_planets_table(self) -> dict:
        planets_data = [
            {
                "Planet": planet.name,
                "Sign": planet.sign,
                "Position": round(float(planet.position), 2),
                "Retrograde": "R" if planet.retrograde else "-",
                "House": planet.house,
            }
            for planet in self.instance.planets_list
        ]
        return {"planets": planets_data}

    def get_houses_table(self) -> dict:
        houses_data = [
            {
                "House": house.name,
                "Sign": house.sign,
                "Position": round(float(house.position), 2),
            }
            for house in self.instance.houses_list
        ]
        return {"houses": houses_data}

    def get_full_report(self) -> str:
        report_data = {
            **self.get_report_title(),
            **self.get_data_table(),
            **self.get_planets_table(),
            **self.get_houses_table()
        }
        return json.dumps(report_data, indent=2)

    def print_report(self) -> None:
        print(self.get_full_report())

if __name__ == "__main__":
    from kerykeion.utilities import setup_logging
    setup_logging(level="debug")

    john = AstrologicalSubject("John", 1975, 10, 10, 21, 15, "Roma", "IT")
    report = Report(john)
    report.print_report()
