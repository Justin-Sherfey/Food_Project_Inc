//
//  Shmeckle.swift
//  Project_Food
//
//  Created by Brett Beattie on 7/8/20.
//  Copyright © 2020 Brett Beattie. All rights reserved.
//

import SwiftUI

struct Shmeckle: View {
    var body: some View {
        VStack(alignment: .leading) {
            Text("Featured")
                .font(.title)
                .fontWeight(.bold)
            ScrollView(.vertical) {
                VStack {
                    RestaurantRow()
                    RestaurantRow()
                    RestaurantRow()
                    RestaurantRow()
                    RestaurantRow()
                    RestaurantRow()
                    RestaurantRow()
                }
            }
        }
    }
}

struct Shmeckle_Previews: PreviewProvider {
    static var previews: some View {
        Shmeckle()
    }
}
