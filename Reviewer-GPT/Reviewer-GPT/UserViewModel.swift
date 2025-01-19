//
//  UserViewModel.swift
//  Reviewer-GPT
//
//  Created by kakao on 1/17/25.
//

import Foundation

class UserViewModel {
    private(set) var user: User
    
    init(user: User) {
        self.user = user
    }
    
    func updateName(_ newName: String) {
        user.name = newName
    }
    
    func updateEmail(_ newEmail: String) {
        user.email = newEmail
    }
    
    func updateBio(_ newBio: String) {
        user.bio = newBio
    }
    
    func userDetails() -> String {
        return """
        Name: \(user.name)
        Email: \(user.email)
        Bio: \(user.bio)
        """
    }
}
