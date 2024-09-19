from dataclasses import asdict, dataclass

import pandas as pd


@dataclass
class Sequence:
    """
    Class for representing a sequence of pulses

    :ivar pulse_interval: Interval between pulses in the sequence (s)
    :ivar pulse_count: Number of pulses in the sequence
    :ivar pulse_train_interval: Interval between pulse trains in the sequence (s)
    :ivar pulse_train_count: Number of pulse trains in the sequence
    """
    pulse_interval: float = 1.0 # s
    pulse_count: int = 1
    pulse_train_interval: float = 1.0 # s
    pulse_train_count: int = 1

    def get_table(self) -> pd.DataFrame:
        """
        Get a table of the sequence parameters

        :returns: Pandas DataFrame of the sequence parameters
        """
        records = [
            {"Name": "Pulse Interval", "Value": self.pulse_interval, "Unit": "s"},
            {"Name": "Pulse Count", "Value": self.pulse_count, "Unit": ""},
            {"Name": "Pulse Train Interval", "Value": self.pulse_train_interval, "Unit": "s"},
            {"Name": "Pulse Train Count", "Value": self.pulse_train_count, "Unit": ""}
        ]
        return pd.DataFrame.from_records(records)

    @staticmethod
    def from_dict(d):
        """
        Create a sequence from a dictionary

        :param d: Dictionary of the sequence parameters
        :returns: Sequence object
        """
        return Sequence(**d)

    def to_dict(self):
        """
        Convert the sequence to a dictionary

        :returns: Dictionary of the sequence parameters
        """
        return asdict(self)
