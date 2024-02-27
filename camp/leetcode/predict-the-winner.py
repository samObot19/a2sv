class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # recursive solutions the player 1 win on the following conditions:
        # In player1 turn, player1 can win by picking either left or right.
        # In player2 turn, player1 wins when player1 have larger score than player2 in both possibilities right and left
        # Base case: when the left < right
        def score(isFirstPlayer, left, right):
            if left >= right:  #base case
                if isFirstPlayer:
                    return nums[left]
                else:
                    return 0
            if isFirstPlayer:
                chooseLeft = score(False, left + 1, right)
                chooseRight = score(False, left, right - 1)
                return max(chooseLeft + nums[left], chooseRight + nums[right])
            else:
                chooseLeft = score(True, left + 1, right)
                chooseRight = score(True, left, right - 1)
                return min(chooseLeft, chooseRight)
            
        sc = score(True, 0, len(nums) - 1)
        return 2*sc >= sum(nums)

        