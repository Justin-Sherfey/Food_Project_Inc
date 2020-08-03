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
    
    var name: String
    var rating: Double
    var tags: Array<String>
}
