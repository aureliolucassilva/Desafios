//Link -> https://www.codewars.com/kata/52a382ee44408cea2500074c

function determinant(m){
    var detResult = 0
    const N = m.length
    
    function matrixTwo(matrix){
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    }

    // 1x1 or 2x2
    if(N == 1){
        detResult = m[0][0]
        return detResult
    } else if(N == 2){
        detResult = matrixTwo(m)
        return detResult
    }
    
    // N > 2
    var signal = 1
    var subMatrixArray = {['N'+ N]: [0, m]}
    var subDetArray = {['N2']: []}
    var exceptColumn = 0

    function subM(matrix){
        var row = []
        var subMatrix = []

        for(rw = 1; rw < matrix.length; rw++){
            for(cl = 0; cl < matrix.length; cl++){
                if(cl != exceptColumn){
                    row.push(matrix[rw][cl])
                }
            }
            subMatrix.push(row)
            row = []
        } 

        return subMatrix
    }
    
    var n = N - 1
    while(n != 1){
        subMatrixArray['N' + n] = []
        for(const value of Object.values(subMatrixArray['N' + (n + 1).toString()])){
            if(Array.isArray(value)){
                for(rep = 0; rep < value.length; rep++){
                    subMatrixArray['N' + n].push(signal * value[0][exceptColumn])
                    subMatrixArray['N' + n].push(subM(value))
                    signal *= -1
                    exceptColumn++
                }
                exceptColumn = 0
                signal = 1
            }
        }
        n--
    }

    for(i = 0; i < subMatrixArray['N2'].length; i += 2){
        subDetArray['N2'].push(subMatrixArray['N2'][i] * matrixTwo(subMatrixArray['N2'][i + 1]))
    }

    n = 3
    var idx = 0
    var subDet = 0
    while(n != N){
        subDetArray['N' + n] = []
        for(const value of Object.values(subMatrixArray['N' + n])){
            if(!Array.isArray(value)){
                for(i = idx; i < n + idx; i++){
                    subDet += subDetArray['N' + (n - 1).toString()][i] * value
                }
                subDetArray['N' + n].push(subDet)
                subDet = 0
                idx += n 
            }
        }
        idx = 0
        n++
    }

    subDetArray['N' + (N - 1).toString()].forEach(value => {
        detResult += value        
    })
    
    return detResult
}
