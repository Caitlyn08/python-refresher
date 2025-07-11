import numpy as np
import math


def calculate_buoyancy(V, density_fluid):
    return V * density_fluid * 9.81


def will_it_float(V, mass):
    density = mass / V
    if density < 1000:
        return True
    return False


def calculate_pressure(depth):
    return 9.81 * depth * 1000


def calculate_acceleration(F, m):
    return F / m


def calculate_angular_acceleration(tau, I):
    return tau / I


def calculate_torque(F_magnitude, F_direction, r):
    return r * F_magnitude * math.sin(math.radians(F_direction))


def calculate_moment_of_inertia(m, r):
    return m * pow(r, 2)


def calculate_auv_acceleration(F_magnitude, F_angle, mass):
    degrees = math.degrees(F_angle)
    components = (
        list[F_magnitude * math.cos(degrees), F_magnitude * math.sin(degrees)] / mass
    )
    return components


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia, thruster_distance
):
    degrees = math.degrees(F_angle)
    torque = F_magnitude * np.sin(degrees) * thruster_distance
    return torque / inertia


def calculate_auv2_acceleration(T, alpha, theta, mass):
    x = []
    y = []
    for i in range(T):
        x.append(T[i] * math.cos(alpha + theta))
        y.append(T[i] * math.sin(alpha + theta))
    xtotal = x[2] + x[3] - x[0] - x[1]
    ytotal = y[0] + y[3] - y[1] - y[2]
    return math.sqrt(xtotal**2 + ytotal**2) / mass


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia):
    distance = np.sqrt(L**2 + l**2)
    torque = distance * -T[0] * np.sin(alpha)
    torque += distance * T[1] * np.sin(alpha)
    torque += distance * -T[2] * np.sin(alpha)
    torque += distance * T[3] * np.sin(alpha)
    return torque / inertia


def simulate_auv2_motion(T, alpha, L, l, mass, inertia, dt, t_final, x0, y0, theta0):
    t = np.array[t_final / dt + 1]
