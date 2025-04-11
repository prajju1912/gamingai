// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BattleScores {
    struct Result {
        string username;
        uint256 score;
        uint256 timestamp;
    }

    Result[] public results;

    function saveResult(string memory _username, uint256 _score) public {
        results.push(Result(_username, _score, block.timestamp));
    }

    function getResult(uint256 index) public view returns (string memory, uint256, uint256) {
        require(index < results.length, "Invalid index");
        Result memory r = results[index];
        return (r.username, r.score, r.timestamp);
    }

    function getTotalResults() public view returns (uint256) {
        return results.length;
    }
}
