def calculate_buoyancy(V, density_fluid):
    return V*density_fluid*9.81

def will_it_float(V, mass):
    density=mass/V
    if density < 1000:
        return True
    return False

def calculate_pressure(depth):
    return 9.81*depth*1000

def calculate_acceleration(F, m):
    return F/m

def calculate_angular_acceleration(tau, I):
    return tau/I

def calculate_torque(F_magnitude, F_direction, r):
    return r*F_magnitude*cos(F_direction)

def calculate_moment_of_inertia(m, r):
    return m*pow(r,2)

