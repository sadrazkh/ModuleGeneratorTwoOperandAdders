def CarrySelect(InBits):
    fullAdder = "module FA(output sum, cout, input a, b, cin);\nwire w0, w1, w2;\n\nxor  (w0, a, b);\nxor  (sum, w0, " \
                "cin);\n\nand  (w1, w0, cin);\nand  (w2, a, b);\n  or  (cout, w1, w2);\nendmodule "
    RippleCarryAdder = "module RCA4(output [3:0] sum, output cout, input [3:0] a, b, input cin);\n\n  wire [3:1] " \
                       "c;\n\n FA fa0(sum[0], c[1], a[0], b[0], cin);\n  fa[2:1](sum[2:1], c[3:2], a[2:1], b[2:1], " \
                       "c[2:1]);\n    fa31(sum[3], cout, a[3], b[3], c[3]);\n\n   endmodule "

    Mux2to1w1="module MUX2to1_w1(output y, input i0, i1, s);\n\n    wire e0, e1;0\n    not #(1) (sn, s);\n\n    and " \
              "#(1) (e0, i0, sn);\n    and #(1) (e1, i1, s);\n\n   or #(1) (y, e0, e1);\n\n    endmodule "

    Mux2to1w4="module MUX2to1_w4(output [3:0] y, input [3:0] i0, i1, input s);\n\n  wire [3:0] e0, e1;\n    not #(1) " \
              "(sn, s);\n\n      and #(1) (e0[0], i0[0], sn);\n    and #(1) (e0[1], i0[1], sn);\n    and #(1) (e0[2], " \
              "i0[2], sn);\n    and #(1) (e0[3], i0[3], sn);\n\n      and #(1) (e1[0], i1[0], s);\n    and #(1) (e1[" \
              "1], i1[1], s);\n    and #(1) (e1[2], i1[2], s);\n    and #(1) (e1[3], i1[3], s);\n\n      or #(1) (y[" \
              "0], e0[0], e1[0]);\n    or #(1) (y[1], e0[1], e1[1]);\n    or #(1) (y[2], e0[2], e1[2]);\n    or #(1) " \
              "(y[3], e0[3], e1[3]);\n\n    endmodule "

    InB1 = str(InBits - 1)
    InB2 = str(InBits - 2)
    
    RippleCarry1 = "module RCAdder1(output [" + InB1 + ":0] sum, output cout, input [" + InB1 + ":0] a, b);\n\n   wire [" + InB1 + ":1] c;\n FA fa0(sum[" \
                    "0], c[1], a[0], b[0], 0);\n  FA fa[" + InB2 + ":1](sum[" + InB2 + ":1], c[" + InB1 + ":2], a[" + InB2 + ":1], b[" + InB2 + ":1], c[" + InB2 + ":1]);\n  FA fa31(sum[" \

    RippleCarry2 = "module RCAdder2(output [" + InB1 + ":0] sum, output cout, input [" + InB1 + ":0] a, b);\n\n   wire [" + InB1 + ":1] c;\n FA fa0(sum[" \
                "0], c[1], a[0], b[0], 0);\n  FA fa[" + InB2 + ":1](sum[" + InB2 + ":1], c[" + InB1 + ":2], a[" + InB2 + ":1], b[" + InB2 + ":1], c[" + InB2 + ":1]);\n  FA fa31(sum[" \


                                                                                                                                                                                                                                                "" + InB1 + "], cout, a[" + InB1 + "], b[" + InB1 + "], c[" + InB1 + "]);\n\n   endmodule "