from juliacall import Main as jl
import julia
jl.println("Hello from Julia!")
cs = jl.cos(1)
jl.println(cs)
sv = jl.seval("1:10")
jl.println(sv)
sn = jl.seval("sin(34)")
jl.println(sn)
