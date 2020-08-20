def AdderGenerator(AdderType, InBits):
    fullAdder = "module FA(output sum, cout, input a, b, cin);\nwire w0, w1, w2;\n\nxor  (w0, a, b);\nxor  (sum, w0, " \
                "cin);\n\nand  (w1, w0, cin);\nand  (w2, a, b);\n  or  (cout, w1, w2);\nendmodule "
    if (AdderType == "RippleCarry"):
        f = open("Adder.v", "a")
        f.write(fullAdder)
        InB1=str(InBits-1)
        InB2=str(InBits-2)
        RippleCarry="module RippleCarry(output ["+InB1+":0] sum, output cout, input ["+InB1+":0] a, b);\n\n   wire ["+InB1+":1] c;\n FA fa0(sum[" \
                "0], c[1], a[0], b[0], 0);\n  FA fa["+InB2+":1](sum["+InB2+":1], c["+InB1+":2], a["+InB2+":1], b["+InB2+":1], c["+InB2+":1]);\n  FA fa31(sum[" \
                ""+InB1+"], cout, a["+InB1+"], b["+InB1+"], c["+InB1+"]);\n\n   endmodule "
        f.write(RippleCarry)

