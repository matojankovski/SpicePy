from scipy.sparse.linalg import spsolve

from Components.BasicComponent import*
from Components.Netlist import*
from Components.Solver import read_netlist

if __name__ == '__main__':
    read_netlist("TestCircuit1.cir")



    # my_circuit = Circuit("New Circle")
    # my_circuit.add_component("V1", 1, 0, "5")
    # my_circuit.add_component("R1", 1, 2, "2k")
    # my_circuit.add_component("R2", 2, 0, "1k")
    # print(my_circuit.components[0])
    # print(my_circuit.create_A_matrix())
    # A = my_circuit.create_A_matrix()
    # print(my_circuit.create_z_matrix())
    # z = my_circuit.create_z_matrix()
    # print(spsolve(A, z))

