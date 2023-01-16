// 1561. Maximum Number of Coins You Can Get

class Solution {
   public:
    int maxCoins(vector<int>& piles) {
        int max_coins = 0;
        int qtd_piles = piles.size() / 3;

        sort(piles.begin(), piles.end());
        for (int i = 0; i < qtd_piles; i++) {
            int coin_position = piles.size() - (i * 2) - 2;
            max_coins += piles[coin_position];
        }

        return max_coins;
    }
};