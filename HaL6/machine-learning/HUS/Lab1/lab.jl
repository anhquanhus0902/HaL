### A Pluto.jl notebook ###
# v0.18.0

using Markdown
using InteractiveUtils

# ╔═╡ 1b4a4dbd-8db9-4e31-a91d-290e3540339d
using PlutoUI

# ╔═╡ edb4f530-9343-450f-b375-cdf5679f6e4d
y = [1,1,2,2,2,1,2,1]

# ╔═╡ 137955df-8da9-43a9-a3e9-2e28e2eac1c6
unique(y)

# ╔═╡ afd3c2e7-8e70-4f02-bbf6-7e6abe1cfeac
K = length(unique(y))

# ╔═╡ 1c95f9bb-d970-4a17-85b4-18bd91899379
N = length(y)

# ╔═╡ a463936f-d278-43ee-abd4-0759943b20b3
θ_k = zeros(K)

# ╔═╡ 7ebf5ee9-c5aa-4b9c-a11a-1325f906cdf1
for k = 1:K
	θ_k[k] = sum(y .== k)
end

# ╔═╡ 6c891bc5-b17f-44bf-907e-c8db7724493f
θ_k

# ╔═╡ 56968bc2-f7e2-4cfe-93f3-857841aa7775
X = [
	1 1 1 0;
	1 1 1 1;
	0 1 1 0;
	0 0 1 1;
	0 0 0 0;
	0 0 0 1;
	1 0 0 0;
	0 1 1 1
]

# ╔═╡ 0206a706-1c21-41e1-8d91-f5117aa7b745
# θ_11 = P(sunny | y = 1)
# θ_12 = P(sunny | y = 2)

# ╔═╡ 11371c1a-365d-4871-bba0-e3d6a9bb99db
id1 = (y .== 1)

# ╔═╡ 40a9f863-3dc7-4b3f-b812-2d49f1faff85
X1 = X[id1, :]

# ╔═╡ a35afa80-7133-4011-bed4-6b6eaec5d705
b1 = sum(X1, dims=1)

# ╔═╡ f80d5e5d-3ebb-4b7c-a83e-a946afc16e01
b1/4

# ╔═╡ 04f4c41c-5271-449a-bd67-46507018ccf7
id2 = (y .== 2)

# ╔═╡ 6c7a7f93-405f-4ebd-b857-24f62023f7ea
X2 = X[id2, :]

# ╔═╡ 9239ab43-d2ee-4251-b5fb-7f84bf302511
b2 = sum(X2, dims=1)

# ╔═╡ 76ad60da-3d78-42f6-8642-6f72460b84c5
b2/4

# ╔═╡ d54574fa-75d9-4ee0-91e9-257390a36c42
D = size(X)[2]

# ╔═╡ e1327515-1a4f-446a-81f1-a05a5e6fd231
θ_jk = zeros(D, K)

# ╔═╡ 3fb2e5ec-2851-428e-b561-d9b1bc0dacfc
for k=1:K
	idk = (y .== k)
	X_k = X[idk, :]
	θ_jk[:, k] = vec(sum(X_k, dims=1))/θ_k[k]
end

# ╔═╡ a3110e72-a09a-470f-b01c-31b10046d155
θ_jk

# ╔═╡ d28b5e9c-1961-4aa0-873a-4952d2584ee1
function train(X, y)
	K = length(unique(y)) # K=2
	N, D = size(X) # N=8, D=4
	θ_k = zeros(K) # [0 0]
	θ_jk = zeros(D, K) # [0 0 ; 0 0 ; 0 0 ; 0 0]
	for k=1:K
		idk = (y .== k)
		θ_k[k] = sum(idk)/N
		X_k = X[idk, :]
		θ_jk[:, k] = vec(sum(X_k, dims=1))/sum(idk)
	end
	return (θ_k, θ_jk)
end 

# ╔═╡ a47fe61f-0168-493a-8a26-8c111b711307
tr = train(X, y)

# ╔═╡ 73ce3127-d72a-4810-9a74-4664471c1f41
function classify(θ_k, θ_jk, xNew)
	# TODO: compute postetior distribution (from likehood and prior)
	# argmax postetior
	D, K = size(θ_jk)
	y_hat, argmax = -1, -1
	for k=1:K
		P_k = θ_k[k]
		for j=1:D
			xNew[j] == 1 ? P_k *= θ_jk[j, k] : P_k *= (1-θ_jk[j, k])
		end
		if P_k > argmax
			y_hat, argmax = k, P_k
		end
	end
	return y_hat
end

# ╔═╡ d6d06298-3650-4c65-b170-3087caddd8fd
classify(tr[1], tr[2], [1 0 1 0])

# ╔═╡ dfebcb89-7d57-421a-9ea7-1a084f9e8273
function evaluate(θ_k, θ_jk, X, y)
	# Step 1: X, θ_k,, θ_jk ==> y_hat
	# Step 2: compare y_hat with y
	return classify(θ_k, θ_jk, X) == y
end

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
PlutoUI = "7f904dfe-b85e-4ff6-b463-dae2292396a8"

[compat]
PlutoUI = "~0.7.34"
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

julia_version = "1.7.2"
manifest_format = "2.0"

[[deps.AbstractPlutoDingetjes]]
deps = ["Pkg"]
git-tree-sha1 = "8eaf9f1b4921132a4cff3f36a1d9ba923b14a481"
uuid = "6e696c72-6542-2067-7265-42206c756150"
version = "1.1.4"

[[deps.ArgTools]]
uuid = "0dad84c5-d112-42e6-8d28-ef12dabb789f"

[[deps.Artifacts]]
uuid = "56f22d72-fd6d-98f1-02f0-08ddc0907c33"

[[deps.Base64]]
uuid = "2a0f44e3-6c83-55bd-87e4-b1978d98bd5f"

[[deps.ColorTypes]]
deps = ["FixedPointNumbers", "Random"]
git-tree-sha1 = "024fe24d83e4a5bf5fc80501a314ce0d1aa35597"
uuid = "3da002f7-5984-5a60-b8a6-cbb66c0b333f"
version = "0.11.0"

[[deps.CompilerSupportLibraries_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "e66e0078-7015-5450-92f7-15fbd957f2ae"

[[deps.Dates]]
deps = ["Printf"]
uuid = "ade2ca70-3891-5945-98fb-dc099432e06a"

[[deps.Downloads]]
deps = ["ArgTools", "LibCURL", "NetworkOptions"]
uuid = "f43a241f-c20a-4ad4-852c-f6b1247861c6"

[[deps.FixedPointNumbers]]
deps = ["Statistics"]
git-tree-sha1 = "335bfdceacc84c5cdf16aadc768aa5ddfc5383cc"
uuid = "53c48c17-4a7d-5ca2-90c5-79b7896eea93"
version = "0.8.4"

[[deps.Hyperscript]]
deps = ["Test"]
git-tree-sha1 = "8d511d5b81240fc8e6802386302675bdf47737b9"
uuid = "47d2ed2b-36de-50cf-bf87-49c2cf4b8b91"
version = "0.0.4"

[[deps.HypertextLiteral]]
git-tree-sha1 = "2b078b5a615c6c0396c77810d92ee8c6f470d238"
uuid = "ac1192a8-f4b3-4bfe-ba22-af5b92cd3ab2"
version = "0.9.3"

[[deps.IOCapture]]
deps = ["Logging", "Random"]
git-tree-sha1 = "f7be53659ab06ddc986428d3a9dcc95f6fa6705a"
uuid = "b5f81e59-6552-4d32-b1f0-c071b021bf89"
version = "0.2.2"

[[deps.InteractiveUtils]]
deps = ["Markdown"]
uuid = "b77e0a4c-d291-57a0-90e8-8db25a27a240"

[[deps.JSON]]
deps = ["Dates", "Mmap", "Parsers", "Unicode"]
git-tree-sha1 = "3c837543ddb02250ef42f4738347454f95079d4e"
uuid = "682c06a0-de6a-54ab-a142-c8b1cf79cde6"
version = "0.21.3"

[[deps.LibCURL]]
deps = ["LibCURL_jll", "MozillaCACerts_jll"]
uuid = "b27032c2-a3e7-50c8-80cd-2d36dbcbfd21"

[[deps.LibCURL_jll]]
deps = ["Artifacts", "LibSSH2_jll", "Libdl", "MbedTLS_jll", "Zlib_jll", "nghttp2_jll"]
uuid = "deac9b47-8bc7-5906-a0fe-35ac56dc84c0"

[[deps.LibGit2]]
deps = ["Base64", "NetworkOptions", "Printf", "SHA"]
uuid = "76f85450-5226-5b5a-8eaa-529ad045b433"

[[deps.LibSSH2_jll]]
deps = ["Artifacts", "Libdl", "MbedTLS_jll"]
uuid = "29816b5a-b9ab-546f-933c-edad1886dfa8"

[[deps.Libdl]]
uuid = "8f399da3-3557-5675-b5ff-fb832c97cbdb"

[[deps.LinearAlgebra]]
deps = ["Libdl", "libblastrampoline_jll"]
uuid = "37e2e46d-f89d-539d-b4ee-838fcccc9c8e"

[[deps.Logging]]
uuid = "56ddb016-857b-54e1-b83d-db4d58db5568"

[[deps.Markdown]]
deps = ["Base64"]
uuid = "d6f4376e-aef5-505a-96c1-9c027394607a"

[[deps.MbedTLS_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "c8ffd9c3-330d-5841-b78e-0817d7145fa1"

[[deps.Mmap]]
uuid = "a63ad114-7e13-5084-954f-fe012c677804"

[[deps.MozillaCACerts_jll]]
uuid = "14a3606d-f60d-562e-9121-12d972cd8159"

[[deps.NetworkOptions]]
uuid = "ca575930-c2e3-43a9-ace4-1e988b2c1908"

[[deps.OpenBLAS_jll]]
deps = ["Artifacts", "CompilerSupportLibraries_jll", "Libdl"]
uuid = "4536629a-c528-5b80-bd46-f80d51c5b363"

[[deps.Parsers]]
deps = ["Dates"]
git-tree-sha1 = "13468f237353112a01b2d6b32f3d0f80219944aa"
uuid = "69de0a69-1ddd-5017-9359-2bf0b02dc9f0"
version = "2.2.2"

[[deps.Pkg]]
deps = ["Artifacts", "Dates", "Downloads", "LibGit2", "Libdl", "Logging", "Markdown", "Printf", "REPL", "Random", "SHA", "Serialization", "TOML", "Tar", "UUIDs", "p7zip_jll"]
uuid = "44cfe95a-1eb2-52ea-b672-e2afdf69b78f"

[[deps.PlutoUI]]
deps = ["AbstractPlutoDingetjes", "Base64", "ColorTypes", "Dates", "Hyperscript", "HypertextLiteral", "IOCapture", "InteractiveUtils", "JSON", "Logging", "Markdown", "Random", "Reexport", "UUIDs"]
git-tree-sha1 = "8979e9802b4ac3d58c503a20f2824ad67f9074dd"
uuid = "7f904dfe-b85e-4ff6-b463-dae2292396a8"
version = "0.7.34"

[[deps.Printf]]
deps = ["Unicode"]
uuid = "de0858da-6303-5e67-8744-51eddeeeb8d7"

[[deps.REPL]]
deps = ["InteractiveUtils", "Markdown", "Sockets", "Unicode"]
uuid = "3fa0cd96-eef1-5676-8a61-b3b8758bbffb"

[[deps.Random]]
deps = ["SHA", "Serialization"]
uuid = "9a3f8284-a2c9-5f02-9a11-845980a1fd5c"

[[deps.Reexport]]
git-tree-sha1 = "45e428421666073eab6f2da5c9d310d99bb12f9b"
uuid = "189a3867-3050-52da-a836-e630ba90ab69"
version = "1.2.2"

[[deps.SHA]]
uuid = "ea8e919c-243c-51af-8825-aaa63cd721ce"

[[deps.Serialization]]
uuid = "9e88b42a-f829-5b0c-bbe9-9e923198166b"

[[deps.Sockets]]
uuid = "6462fe0b-24de-5631-8697-dd941f90decc"

[[deps.SparseArrays]]
deps = ["LinearAlgebra", "Random"]
uuid = "2f01184e-e22b-5df5-ae63-d93ebab69eaf"

[[deps.Statistics]]
deps = ["LinearAlgebra", "SparseArrays"]
uuid = "10745b16-79ce-11e8-11f9-7d13ad32a3b2"

[[deps.TOML]]
deps = ["Dates"]
uuid = "fa267f1f-6049-4f14-aa54-33bafae1ed76"

[[deps.Tar]]
deps = ["ArgTools", "SHA"]
uuid = "a4e569a6-e804-4fa4-b0f3-eef7a1d5b13e"

[[deps.Test]]
deps = ["InteractiveUtils", "Logging", "Random", "Serialization"]
uuid = "8dfed614-e22c-5e08-85e1-65c5234f0b40"

[[deps.UUIDs]]
deps = ["Random", "SHA"]
uuid = "cf7118a7-6976-5b1a-9a39-7adc72f591a4"

[[deps.Unicode]]
uuid = "4ec0a83e-493e-50e2-b9ac-8f72acf5a8f5"

[[deps.Zlib_jll]]
deps = ["Libdl"]
uuid = "83775a58-1f1d-513f-b197-d71354ab007a"

[[deps.libblastrampoline_jll]]
deps = ["Artifacts", "Libdl", "OpenBLAS_jll"]
uuid = "8e850b90-86db-534c-a0d3-1478176c7d93"

[[deps.nghttp2_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "8e850ede-7688-5339-a07c-302acd2aaf8d"

[[deps.p7zip_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "3f19e933-33d8-53b3-aaab-bd5110c3b7a0"
"""

# ╔═╡ Cell order:
# ╠═edb4f530-9343-450f-b375-cdf5679f6e4d
# ╠═137955df-8da9-43a9-a3e9-2e28e2eac1c6
# ╠═afd3c2e7-8e70-4f02-bbf6-7e6abe1cfeac
# ╠═1c95f9bb-d970-4a17-85b4-18bd91899379
# ╠═a463936f-d278-43ee-abd4-0759943b20b3
# ╠═7ebf5ee9-c5aa-4b9c-a11a-1325f906cdf1
# ╠═6c891bc5-b17f-44bf-907e-c8db7724493f
# ╠═56968bc2-f7e2-4cfe-93f3-857841aa7775
# ╠═0206a706-1c21-41e1-8d91-f5117aa7b745
# ╠═11371c1a-365d-4871-bba0-e3d6a9bb99db
# ╠═40a9f863-3dc7-4b3f-b812-2d49f1faff85
# ╠═a35afa80-7133-4011-bed4-6b6eaec5d705
# ╠═f80d5e5d-3ebb-4b7c-a83e-a946afc16e01
# ╠═04f4c41c-5271-449a-bd67-46507018ccf7
# ╠═6c7a7f93-405f-4ebd-b857-24f62023f7ea
# ╠═9239ab43-d2ee-4251-b5fb-7f84bf302511
# ╠═76ad60da-3d78-42f6-8642-6f72460b84c5
# ╠═d54574fa-75d9-4ee0-91e9-257390a36c42
# ╠═e1327515-1a4f-446a-81f1-a05a5e6fd231
# ╠═3fb2e5ec-2851-428e-b561-d9b1bc0dacfc
# ╠═a3110e72-a09a-470f-b01c-31b10046d155
# ╠═1b4a4dbd-8db9-4e31-a91d-290e3540339d
# ╠═d28b5e9c-1961-4aa0-873a-4952d2584ee1
# ╠═a47fe61f-0168-493a-8a26-8c111b711307
# ╠═73ce3127-d72a-4810-9a74-4664471c1f41
# ╠═d6d06298-3650-4c65-b170-3087caddd8fd
# ╠═dfebcb89-7d57-421a-9ea7-1a084f9e8273
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
