## 1. r = l + k -1

## 2. k = r - l + 1

## 3. S(l+1, r+1) = S(l, r) - A[i] + A[i+1]

## 
$$
S_l=\sum_{i=l}^{l+k-1}A[i]
$$

## 
$$
\boxed{
\begin{aligned}
S_0&=\sum_{i=0}^{k-1}A[i]\\[5pt]
S_{l+1}&=S_l-A[l]+A[l+k]
\end{aligned}
}
$$

 ## Sₗ₊₁ = Sₗ - A[l] + A[l+k]

## 
$$
V(l,r)=
\begin{cases}
\text{True}, & \text{window satisfies constraints}\\
\text{False}, & \text{otherwise}
\end{cases}
$$

$$
r\leftarrow r+1
$$

$$
l\leftarrow l+1
$$

$$
\boxed{
M\leftarrow\max(M,r-l+1)
}
$$