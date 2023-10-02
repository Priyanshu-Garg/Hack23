import math

def hohmann_transfer_parameters(r1, r2):
    """
    Calculate the delta-v and transfer time for a Hohmann transfer orbit.

    Args:
    - r1: Radius of the initial circular orbit (in meters).
    - r2: Radius of the target circular orbit (in meters).

    Returns:
    - delta_v: Delta-v required for the transfer (in meters per second).
    - transfer_time: Time of transfer (in seconds).
    """
    mu = 3.986 * 10**14  # Standard gravitational parameter for Earth (in m^3/s^2)

    # Calculate the semi-major axes of the initial and target orbits
    a1 = r1
    a2 = r2

    # Calculate the velocity of the initial and target orbits
    v1 = math.sqrt(mu / a1)
    v2 = math.sqrt(mu / a2)

    # Calculate the delta-v required for the transfer
    delta_v = v2 - v1

    # Calculate the transfer time
    transfer_time = math.pi * math.sqrt((a1 + a2)**3 / (8 * mu))

    return delta_v, transfer_time

# Example usage:
initial_radius = 800000  # 800 km altitude above Earth's surface
target_radius = 1200000  # 1200 km altitude above Earth's surface

delta_v, transfer_time = hohmann_transfer_parameters(initial_radius, target_radius)

print(f"Delta-v required: {delta_v:.2f} m/s")
print(f"Transfer time: {transfer_time:.2f} seconds")
