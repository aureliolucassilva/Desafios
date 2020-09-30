# Link -> https://www.codewars.com/kata/583203e6eb35d7980400002a

def count_smileys(arr):
   number_smiles = 0

   for smiley_face in arr:
        if (":" in smiley_face) or (";" in smiley_face):
            if (")" in smiley_face) or ("D" in smiley_face):
                if len(smiley_face) > 2:
                    if ("-" in smiley_face) or ("~" in smiley_face):
                        number_smiles += 1
                else:
                    number_smiles += 1

   return number_smiles
