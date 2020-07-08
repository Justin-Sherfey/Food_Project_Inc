//
//  Restaurant.swift
//  Project_Food
//
//  Created by Brett Beattie on 7/8/20.
//  Copyright © 2020 Brett Beattie. All rights reserved.
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
