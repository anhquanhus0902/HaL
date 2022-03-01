#!/usr/bin/env julia

using DelimitedFiles
using Statistics

function readData(path)
    A = readdlm(path, ',')
    X = A[:, 3:12]
    y = Int.(A[:, 2]) .+ 1
    return (X, y)
end

X, y = readData("wdbc.txt")

#id1 = (y .== 1)
#X1 = X[id1, :]
#id2 = (y .== 2)
#X2 = X[id2, :]

function train(X, y)
    K = length(unique(y))
    N, D = size(X)
    muy = zeros(D, K)
    sigma = zeros(D, K)
    theta = zeros(K)

    for k=1:K
        idk = (y .== k)
        muy[:, k] = vec(mean(X[idk, :], dims=1))
        sigma[:, k] = vec(std(X[idk, :], dims=1))
        theta[k] = sum(idk)/N

    end
    return (muy, sigma, theta)
end    

function classify(muy, sigma, theta, xNew)
    D, K = size(muy)
    scores = zeros(K)
    for k=1:K
        scores[k] = theta[k]
        for j=1:D
            scores[k] += log( 1/sqrt(2*pi*sigma[j,k]^2)) - (xNew[j]-muy[j,k])^2/(2*sigma[j,k]^2)
        end
    end
    return argmax(scores)
end    

function evaluate(muy, sigma, theta, X, y)
    N = length(y)
    z = map(i -> classify(muy, sigma, theta, X[i,:]), 1:N)
    return sum(z .== y)/N
end

a = train(X,y)
print(evaluate(a[1], a[2], a[3], X, y))
#print(classify(a[1], a[2], a[3], [8.196,16.84,51.71,201.9,0.086,0.05943,0.01588,0.005917,0.1769,0.06503,0.1563,0.9567,1.094,8.205,0.008968,0.01646,0.01588,0.005917,0.02574,0.002582,8.964,21.96,57.26,242.2,0.1297,0.1357,0.0688,0.02564,0.3105,0.07409]))
#display(train(X,y)[1])
#display(train(X,y)[2])
#display(train(X,y)[3])
