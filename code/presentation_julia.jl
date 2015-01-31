julia> f(x) = x * x
f (generic function with 1 method)

julia> code_llvm(f, (Float64,))

define double @julia_f_20166(double) {
top:
  %1 = fmul double %0, %0, !dbg !857
  ret double %1, !dbg !857
}

julia> code_native(f, (Float64,))
        .text
Filename: none
Source line: 1
        push    RBP
        mov     RBP, RSP
Source line: 1
        mulsd   XMM0, XMM0
        pop     RBP
        ret

julia> code_native(f, (Int,))
        .text
Filename: none
Source line: 1
        push    RBP
        mov     RBP, RSP
Source line: 1
        imul    RDI, RDI
        mov     RAX, RDI
        pop     RBP
        ret

