from typing import Any


def CarrySelect(InBits):
    fullAdder = "module FA(output sum, cout, input a, b, cin);\nwire w0, w1, w2;\n\nxor  (w0, a, b);\nxor  (sum, w0, " \
                "cin);\n\nand  (w1, w0, cin);\nand  (w2, a, b);\n  or  (cout, w1, w2);\nendmodule "

    Mux2to1 = "module m21(Y, D0, D1, S);\n\n    output Y;\n  input D0, D1, S;\n  wire T1, T2, Sbar;\n\n    and (T1, " \
              "D1, S), (T2, D0, Sbar);\n  not (Sbar, S);\n  or (Y, T1, T2);\n\n    endmodule "

    InB1 = str(InBits - 1)
    InB2 = str(InBits - 2)

    RippleCarry1 = "module RCAdder(output [" + InB1 + ":0] sum, output cout, input [" + InB1 + ":0] a, b,input cin);\n\n   wire [" + InB1 + ":1] c;\n FA fa0(sum[" \
                                                                                                                                            "0], c[1], a[0], b[0], cin);\n  FA fa[" + InB2 + ":1](sum[" + InB2 + ":1], c[" + InB1 + ":2], a[" + InB2 + ":1], b[" + InB2 + ":1], c[" + InB2 + ":1]);\n  FA fa31(sum[" \
                                                                                                                                                                                                                                                                                             "" + InB1 + "], cout, a[" + InB1 + "], b[" + InB1 + "], c[" + InB1 + "]);\n\n   endmodule "

    CarrySelctAdder = "module CSAdder(output [" + InB1 + ":0] sum, output cout, input [" + InB1 + ":0] a, b,input " \
                                                                                                  "cin);\n\n   wire[" \
                      + InB1 + ":0]  sum0, sum1;\n  wire  c1, c2;\n  RCAdder RCA1(sum0,c1,a,b,0);\n  RCAdder RCA2(" \
                               "sum1,c2,a,b,1);\n  m21 muxs[InB1:0](sum,sum0,sum1,cin);\n  m21 coutmux(cout,c1,c2," \
                               "cin);\n\n  endmodule "

    fileName = "CarrySelect_Adder" + str(InBits) + ".v"
    f = open(fileName, "a")
    f.write(fullAdder)
    f.write(Mux2to1)
    f.write(RippleCarry1)
    f.write(CarrySelctAdder)
    f.close()
