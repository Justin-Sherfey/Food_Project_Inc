//
//  Restaurant.swift
//  MealMeister
//
//  Created by Justin Sherfey on 7/10/20.
//  Copyright © 2020 Andrew Thomas. All rights reserved.
//

import Foundation

struct Restaurant: Identifiable {
    var id: String = UUID().uuidString
    
    var displayName: String
    var name: String
    var tag: String
}
