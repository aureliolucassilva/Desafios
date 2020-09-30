//Link -> https://www.codewars.com/kata/597cfe0a38015079a0000006

function coveredPawns(pawns){
    const boardColumns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
    const boardLines = ['1', '2', '3', '4', '5', '6', '7', '8'];
    var protectedPawns = 0;

    for(const pawnPosition of pawns){
        var indexA = 0;
        var indexB = 0;
        var indexC = 0;

        if(pawnPosition[1] != '1'){
            if(pawnPosition[0] != 'a' && pawnPosition[0] != 'h'){
                indexA = boardColumns.indexOf(pawnPosition[0]) - 1;
                indexB = boardColumns.indexOf(pawnPosition[0]) + 1;
                indexC = boardLines.indexOf(pawnPosition[1]) - 1;

                var pawn1 = boardColumns[indexA] + boardLines[indexC];
                var pawn2 = boardColumns[indexB] + boardLines[indexC];

                if(pawns.includes(pawn1) || pawns.includes(pawn2)) protectedPawns++;

            } else if(pawnPosition[0] == 'a'){
                indexB = boardColumns.indexOf(pawnPosition[0]) + 1;
                indexC = boardLines.indexOf(pawnPosition[1]) - 1;

                var pawn2 = boardColumns[indexB] + boardLines[indexC];

                if(pawns.includes(pawn2)) protectedPawns++;

            } else if(pawnPosition[0] == 'h'){
                indexA = boardColumns.indexOf(pawnPosition[0]) - 1;
                indexC = boardLines.indexOf(pawnPosition[1]) - 1;

                var pawn1 = boardColumns[indexA] + boardLines[indexC];

                if(pawns.includes(pawn1)) protectedPawns++;
            }
        }
    }

    return protectedPawns;
}
