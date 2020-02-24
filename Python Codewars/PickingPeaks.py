# In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

# For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

# The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

# All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

# The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)

#Have fun!
def pick_peaks(arr):
  ret={"pos":[] , "peaks":[]}
  j=0  
  pos = iter(arr)
  preval =0
  plateau=0
  for index,value in enumerate(arr):
    if index!=len(arr)-1 and index!=0:
        preval=arr[index-1]
        nextval=arr[index+1]
        if (value>preval and value>nextval):
              print(value)
              current_pos=index
              current_peak=value
              ret["pos"].append(int(index))
              ret["peaks"].append(int(value))
              plateau=1
        if (value>preval and value==nextval):
              current_peak=value
              current_pos=index
              plateau=1
        if (value==preval and value>nextval and plateau==1):
              print(value)
              for i in ret["pos"]:
                  if i==current_pos:
                      break;
              else:
                  ret["pos"].append(int(current_pos))
                  ret["peaks"].append(int(current_peak))
              plateau=0
        
    else:
        continue
  list(ret["pos"])
  return ret