#!/usr/bin/env julia

using DelimitedFiles
#using Plots

function readData(filePath)
    A = readdlm(filePath, ',')
    X = A[:, 3:12]
    y = Int.(A[:, 2])
    return (X, y)
end

sigmoid(u) = 1.0 / (1.0 + exp(-u))
h(x) = sigmoid(x)

function negativeLogLikelihood(X, y, theta)
    N = length(y)
    res = 0
    for i in 1:N
        h_x = h(theta' * X[i,:])
        res += y[i]*log(h_x) + (1-y[i])*log(1-h_x)
    end
    return -res
end

function gradientDescent(X, y, maxIters=1000, alpha=0.001)
	N, Dp1 = size(X)
	theta = zeros(Dp1)
    for i in 1:maxIters
        
		theta -= alpha*d
    end
    return theta
end

function main()
    X, y = readData("./wdbc.txt")
    theta = gradientDescent(X, y)
	print(theta)
	
    #l = negativeLogLikelihood(X, y)
end
main()
