def CarryLookAhead(b, path):
    inbit1 = str(b - 1)
    pggen = "module PGGen(output g, p, input a, b);\n\n  and #(1) (g, a, b);\n  xor #(2) (p, a, b);\n     endmodule\n"
    CarryLA = "module CLA(output [" + inbit1 + ":0] sum, output cout, input [" + inbit1 + ":0] a, b);\n\n"
    CarryLA += "   wire [" + inbit1 + ":0] g, p, c;\n   wire [" + str(
        (b * (b + 1)) / 2 - 1) + ":0] e;\n    wire cin;\n     buf #(1) (cin, 0);\n\n      "
    for i in range(b):
        CarryLA += "and #(1) (e[" + str(i * (i + 1) / 2) + "], cin"
        for j in range(i + 1):
            CarryLA += ", p[" + str(j) + "]"
        CarryLA += ");\n"
        for k in range(i):
            CarryLA += "  and #(1) (e[" + str((i * (i + 1) / 2) + 1) + "], g[" + str(k) + "]"
            for m in range(i - k - 1):
                CarryLA += ", p[" + str(m + 1) + "]"
            CarryLA += ");\n"
        CarryLA += "  or #(1) (c[" + str(i) + "]"
        for f in range(i + 1):
            CarryLA += ", e[" + str((i * (i + 1) / 2 + f)) + "]"
        CarryLA += ", g[" + str(i) + "]);"
        CarryLA += "\n\n"
    CarryLA += "xor #(2) (sum[0],p[0],cin);"
    CarryLA += "xor #(2) x[:1](sum[" + inbit1 + ":1],p[" + inbit1 + ":1],c[" + str(
        b - 2) + ":0]);\n    buf #(1) (cout, c[" + inbit1 + "]);\n     PGGen pggen[" + inbit1 + ":0](g[" + inbit1 + ":0],p[" + inbit1 + ":0],a[" + inbit1 + ":0],b[" + inbit1 + ":0]);\n  endmodule"

    if path != "None":
        fileName = str(path) + "CarryLA_Adder" + str(b) + ".v"
    else:
        fileName = "CarryLA_Adder" + str(b) + ".v"

    n = open(fileName, "a")
    n.write(pggen)
    n.write(CarryLA)
    n.close()
