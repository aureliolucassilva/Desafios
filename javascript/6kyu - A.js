//Link -> https://www.codewars.com/kata/566be96bb3174e155300001b

function maxBall(v0) {
    const v1 = v0 / 3.6
    const t = v1 / (2 * 0.5 * 9.81)
    return Math.round(t * 10)
}
