#!/usr/bin/env julia

function cal(Xj)
    avg = mean(Xj)
    variance = 

function train(X, y)
    K = length(unique(y))
    N, D = length(X), length(X[1])

    thetaK = zeros(K)
    thetaJK = zeros(D, K)
    for k=1:K
        idk = (y .== k-1)
        thetaK[k] = sum(idk)/N

    end

    return thetaK
end    

function test(X)
    return -1
end   

X, y = [], []
lines = readlines("wdbc.txt")
for line in lines
    spl = parse.(Float64, split(line, ","))
    push!(X, spl[3:12])
    push!(y, spl[2])
end   

print(train(X,y))
