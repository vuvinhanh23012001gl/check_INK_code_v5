class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def to_dict(self):
        return {"x": self.x, "y": self.y, "z": self.z}

    @classmethod
    def from_dict(cls, data):
        return cls(data["x"], data["y"], data["z"])
    

class RunPath:
    def __init__(self, id: str):
        self.id = id
        self.points: list[Point] = []

    def add_point(self, x: float, y: float, z: float):
        self.points.append(Point(x, y, z))

    def get_points(self):
        return self.points
    
    def to_dict(self):
        return {
            "id": self.id,
            "points": [p.to_dict() for p in self.points]
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls(data["id"])
        obj.points = [
            Point.from_dict(p)
            for p in data.get("points", [])
        ]
        return obj
    