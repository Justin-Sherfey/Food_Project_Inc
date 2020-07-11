//
//  Restaurant.swift
//  MealMeister
//
//  Created by Justin Sherfey on 7/10/20.
//  Copyright © 2020 Andrew Thomas. All rights reserved.
//

import SwiftUI
import CoreLocation

struct Restaurant: Hashable, Codable, Identifiable {
    var id: Int
    var name: String
    fileprivate var imageName: String
    var isFavorite: Bool
    var isFeatured: Bool

    enum Category: String, CaseIterable, Codable, Hashable {
        case featured = "Featured"
    }
}

extension Restaurant {
    var image: Image {
        ImageStore.shared.image(name: imageName)
    }
}
